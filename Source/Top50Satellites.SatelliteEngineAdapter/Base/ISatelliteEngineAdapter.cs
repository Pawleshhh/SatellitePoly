namespace Top50Satellites.SatelliteEngineAdapter;

/// <summary>
/// Interface for accessing satellite engine implementation.
/// </summary>
public interface ISatelliteEngineAdapter
{

    /// <summary>
    /// Gets given satellite data's age.
    /// </summary>
    /// <param name="utcDateTime">Utc date time to be compared with given satellite data.</param>
    /// <param name="satellite">Satellite data to be compared with given utcDateTime.</param>
    /// <returns>Age of satellite data as <see cref="TimeSpan"/></returns>
    Task<TimeSpan> GetSatelliteDataAge(DateTime utcDateTime, TleData satellite);
    
    /// <summary>
    /// Gets collection of satellite data from given path.
    /// </summary>
    /// <param name="tlePath">Path to tle data.</param>
    /// <returns>Returns collection of satellite data.</returns>
    Task<IEnumerable<TleData>> GetSatellites(string tlePath);

}
