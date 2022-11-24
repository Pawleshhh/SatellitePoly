using Python.Runtime;
using Top50Satellites.Common;
using static Top50Satellites.Common.ResourceHelper;

namespace Top50Satellites.SatelliteEngineAdapter;

/// <summary>
/// Python engine for satellite calculations.
/// </summary>
internal class PythonEngineAdapter : ISatelliteEngineAdapter
{

    #region Fields

    private readonly Lazy<string> pythonCode =
        new Lazy<string>(() => ReadResource<PythonEngineAdapter>("Top50Satellites.SatelliteEngineAdapter.Python.SatelliteEngine.py"));

    #endregion

    #region Constructors

    public PythonEngineAdapter(string pythonDllPath)
    {
        Runtime.PythonDLL = pythonDllPath;
        PythonEngine.Initialize();
        PythonEngine.BeginAllowThreads();
    }

    #endregion

    #region ISatelliteEngineAdapter

    /// <inheritdoc/>
    public Task<TimeSpan> GetSatelliteDataAge(DateTime utcDateTime, TleData satellite)
    {
        throw new NotImplementedException();
        //return Task.Run(() => Work<TimeSpan>(m => m.howOldInDays(
        //    utcDateTime.Year,
        //    utcDateTime.Month,
        //    utcDateTime.Day,
        //    utcDateTime.Hour,
        //    utcDateTime.Minute,
        //    utcDateTime.Second,
        //    satellite.Epoch)));
    }

    /// <inheritdoc/>
    public Task<IEnumerable<TleData>> GetSatellites(string tlePath)
    {
        return Task.Run(() => Work<IEnumerable<TleData>>(m =>
        {
            dynamic result = m.getSatellites(tlePath);

            List<TleData> tleList = new();
            foreach(dynamic data in result)
            {
                tleList.Add(new TleData(
                    (double)data.epoch.ut1,
                    (string)data.name,
                    (int)data.model.satnum,
                    (string)data.model.classification,
                    (string)data.model.intldesg,
                    (int)data.model.epochyr,
                    (double)data.model.epochdays,
                    (double)data.model.jdsatepoch,
                    (double)data.model.ndot,
                    (double)data.model.nddot,
                    (double)data.model.bstar,
                    (int)data.model.ephtype,
                    (int)data.model.elnum,
                    (double)data.model.inclo,
                    (double)data.model.nodeo,
                    (double)data.model.ecco,
                    (double)data.model.argpo,
                    (double)data.model.mo,
                    (double)data.model.no_kozai,
                    (int)data.model.revnum));
            }

            return tleList;
        }));
    }

    #endregion

    #region PythonNET

    private void Work(Action<dynamic> action)
    {
        using (Py.GIL())
        {
            using (var scope = Py.CreateScope())
            {
                action(scope.Exec(pythonCode.Value));
            }
        }
    }

    private T Work<T>(Func<dynamic, dynamic> func)
    {
        using (Py.GIL())
        {
            using (var scope = Py.CreateScope())
            {
                return (T)func(scope.Exec(pythonCode.Value));
            }
        }
    }

    private T Work<T>(Func<dynamic, T> func)
    {
        using (Py.GIL())
        {
            using (var scope = Py.CreateScope())
            {
                return func(scope.Exec(pythonCode.Value));
            }
        }
    }

    #endregion

}
