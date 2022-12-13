namespace Top50Satellites.SatelliteServiceWrapper;

public interface IServiceWrapper : IDisposable
{

    public void Initialize();
    public void Execute(Action action);
    public Task ExecuteAsync(Action action);
    public T Execute<T>(Func<T> func);
    public Task<T> ExecuteAsync<T>(Func<T> func);

}
