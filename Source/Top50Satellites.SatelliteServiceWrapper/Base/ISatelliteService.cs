using Top50Satellites.Common;

namespace Top50Satellites.SatelliteServiceWrapper;

public interface ISatelliteService
{

    public IPolyData GetPolynomials(
        int satelliteId,
        ICoordinateSystem3D<double> observer,
        DateTimeOffset start,
        int interval,
        int degrees);

}
