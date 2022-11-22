namespace Top50Satellites.SatelliteEngineAdapter;

/// <summary>
/// Two-line element set record.
/// </summary>
/// <param name="Epoch">Exact epoch moment for the satellite orbit parameters.</param>
/// <param name="Name">Satellite name.</param>
/// <param name="SatelliteNumber">The unique satellite NORAD catalog number given in the TLE file.</param>
/// <param name="SatelliteClassification">Satellite classification.</param>
/// <param name="InternationalDesignator">International designator.</param>
/// <param name="EpochYear">Full four-digit year of this element set’s epoch moment.</param>
/// <param name="EpochDays">Fractional days into the year of the epoch moment.</param>
/// <param name="JulianDateOfEpoch">Julian date of the epoch.</param>
/// <param name="FirstTimeDerivativeOfMeanMotion">First time derivative of the mean motion.</param>
/// <param name="SecondTimeDerivativeOfMeanMotion">Second time derivative of the mean motion.</param>
/// <param name="BStar">Ballistic drag coefficient B* in inverse earth radii.</param>
/// <param name="EphemerisType">Ephemeris type.</param>
/// <param name="ElementNumber">Element number.</param>
/// <param name="Inclination">Inclination in radians.</param>
/// <param name="RightAscensionOfAscendingNode">Right ascension of ascending node in radians.</param>
/// <param name="Eccentricity">Eccentricity.</param>
/// <param name="ArgumentOfPerigee">Argument of perigee in radians.</param>
/// <param name="MeanAnomaly">Mean anomaly in radians.</param>
/// <param name="MeanMotion">Mean motion in radians per minute.</param>
/// <param name="RevolutionNumber">Revolution number at epoch.</param>
public record TleData(
    double Epoch,
    string Name,
    int SatelliteNumber,
    string SatelliteClassification,
    string InternationalDesignator,
    int EpochYear,
    double EpochDays,
    double JulianDateOfEpoch,
    double FirstTimeDerivativeOfMeanMotion,
    double SecondTimeDerivativeOfMeanMotion,
    double BStar,
    int EphemerisType,
    int ElementNumber,
    double Inclination,
    double RightAscensionOfAscendingNode,
    double Eccentricity,
    double ArgumentOfPerigee,
    double MeanAnomaly,
    double MeanMotion,
    int RevolutionNumber);

/// <summary>
/// Satellite classification used in <see cref="TleData"/>.
/// </summary>
public enum SatelliteClassification
{
    /// <summary>
    /// Unknown satellite
    /// </summary>
    Unknown,
    /// <summary>
    /// Unclassified satellite.
    /// </summary>
    Unclassified,
    /// <summary>
    /// Classified satellite.
    /// </summary>
    Classified,
    /// <summary>
    /// Secret satellite.
    /// </summary>
    Secret
}