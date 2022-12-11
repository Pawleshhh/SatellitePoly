using Python.Runtime;

namespace Top50Satellites.SatelliteServiceWrapper;

internal class PythonWrapper : IServiceWrapper
{

    #region Fields

    private static readonly string dllPath = "C:\\Program Files\\Python311\\python311.dll";

    #endregion

    #region Constructors

    static PythonWrapper()
    {
        Runtime.PythonDLL= dllPath;
        PythonEngine.Initialize();
    }

    #endregion

    #region Properites

    #endregion

    #region Methods

    public T Execute<T>(string exec, params object[] parameters)
    {
        throw new NotImplementedException();
    }

    #endregion

    #region Private methods

    #endregion

}
