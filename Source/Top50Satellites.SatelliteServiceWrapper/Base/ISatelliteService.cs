using Top50Satellites.Common;

namespace Top50Satellites.SatelliteServiceWrapper;

public interface ISatelliteService
{

    public IDictionary<SatellitePolyData, IPolyData> GetPolynomials(
        EarthSatellite earthSatellite,
        ICoordinateSystem3D<double> observer,
        DateTimeOffset start,
        TimeSpan interval,
        int degrees);

}

public enum SatellitePolyData
{
    Altitude,
    Azimuth,
    Elevation
}