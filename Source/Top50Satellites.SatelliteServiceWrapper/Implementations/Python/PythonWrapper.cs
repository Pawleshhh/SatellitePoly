using Python.Runtime;
using System;

namespace Top50Satellites.SatelliteServiceWrapper;

internal class PythonWrapper : IServiceWrapper
{

    #region Fields

    /// <summary>
    /// TODO: Automatically search for it (env. variables)
    /// </summary>
    private static readonly string dllPath = "C:\\Program Files\\Python311\\python311.dll";

    #endregion

    #region Methods

    public void Initialize()
    {
        Runtime.PythonDLL = dllPath;
        PythonEngine.Initialize();
        PythonEngine.BeginAllowThreads();
    }

    public void Execute(Action action)
    {
        using (Py.GIL())
        {
            action();
        }
    }

    public Task ExecuteAsync(Action action)
    {
        using (Py.GIL())
        {
            return Task.Run(action);
        }
    }
    public T Execute<T>(Func<T> func)
    {
        using (Py.GIL())
        {
            return func();
        }
    }
    public Task<T> ExecuteAsync<T>(Func<T> func)
    {
        using (Py.GIL())
        {
            return Task.Run(func);
        }
    }

    public virtual void Dispose() { }

    #endregion

    #region Private methods

    #endregion

}
