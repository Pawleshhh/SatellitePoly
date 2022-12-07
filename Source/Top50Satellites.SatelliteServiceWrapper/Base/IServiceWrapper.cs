namespace Top50Satellites.SatelliteServiceWrapper;

public interface IServiceWrapper
{

    public T Execute<T>(string exec, params object[] parameters);

}
