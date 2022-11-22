using System.Reflection;

namespace Top50Satellites.Common;

public static class ResourceHelper
{

    public static string ReadResource<T>(string path)
    {
        var assembly = typeof(T).GetTypeInfo().Assembly;
        Stream? resource = assembly.GetManifestResourceStream(path);
        if (resource == null)
        {
            return string.Empty;
        }

        using var reader = new StreamReader(resource);

        return reader.ReadToEnd();
    }

}
