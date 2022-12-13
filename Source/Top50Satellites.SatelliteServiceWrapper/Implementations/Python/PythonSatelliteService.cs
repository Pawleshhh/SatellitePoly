using Python.Runtime;
using Top50Satellites.Common;

namespace Top50Satellites.SatelliteServiceWrapper;

internal class PythonSatelliteService : ISatelliteService
{

    #region Constructors

    public PythonSatelliteService()
    {

    }

    #endregion

    #region Properties

    private PythonWrapper pythonServiceWrapper;

    protected PythonWrapper PythonServiceWrapper
    {
        get
        {
            if (pythonServiceWrapper == null)
            {
                pythonServiceWrapper = new();
                pythonServiceWrapper.Initialize();
            }

            return pythonServiceWrapper;
        }
    }

    #endregion

    #region Methods

    public IDictionary<SatellitePolyData, IPolyData> GetPolynomials(
        EarthSatellite earthSatellite, 
        ICoordinateSystem3D<double> observer, 
        DateTimeOffset start, 
        TimeSpan interval, 
        int degrees)
    {
        if (degrees < 2)
        {
            throw new ArgumentException(nameof(degrees));
        }

        int seconds = interval.Seconds;
        string formattedDate = start.ToString("dd/M/yyyy H:m:s z");

        PythonServiceWrapper.Execute(() =>
        {
            dynamic service = Py.Import("satelliteservice");
            dynamic skyfield = Py.Import("skyfield.api");
            dynamic satellite = GetEarthSatellite(skyfield, earthSatellite);
            dynamic ts = skyfield.load.timescale();
            dynamic coords = skyfield.wgs84.latlon(
                skyfield.N * observer.X, 
                skyfield.W * observer.Y, 
                observer.Z);

            dynamic dateutilParser = Py.Import("dateutil.parser");
            dynamic startDate = dateutilParser.parse(formattedDate);

            dynamic polyList = service.polynomials.get_polynomials_of_horizon_position(
                ts,
                startDate,
                seconds,
                coords,
                satellite,
                degrees);

            ; //Debug me
        });

        return null;
    }

    #endregion

    #region Private methods

    private static dynamic GetEarthSatellite(dynamic module, EarthSatellite earthSatellite)
    {
        return module.EarthSatellite(earthSatellite.Line1, earthSatellite.Line2);
    }

    #endregion

}
