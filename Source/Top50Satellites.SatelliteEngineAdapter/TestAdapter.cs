using Python.Runtime;
using System.Reflection;

namespace Top50Satellites.SatelliteEngineAdapter;

public static class TestAdapter
{

    public static void Foo()
    {
        string pythonSrc = ReadResource("Top50Satellites.SatelliteEngineAdapter.SatelliteEngine.py");

        Runtime.PythonDLL = @"C:\Program Files\Python311\python311.dll";
        PythonEngine.Initialize();

        using (Py.GIL())
        {
            using (var scope = Py.CreateScope())
            {
                dynamic module = scope.Exec(pythonSrc);
                dynamic result = module.getMarsPosition();

                var mars = (double[])result;
            }
        }
    }

    private static string ReadResource(string path)
    {
        var assembly = typeof(TestAdapter).GetTypeInfo().Assembly;
        Stream? resource = assembly.GetManifestResourceStream(path);
        if (resource == null)
        {
            return string.Empty;
        }

        using var reader = new StreamReader(resource);

        return reader.ReadToEnd();
    }

}
