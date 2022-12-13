using Top50Satellites.Common;

namespace Top50Satellites.SatelliteServiceWrapper;

internal class PythonSatelliteServiceTests
{

    #region Tests

    [Test]
    public async Task Test()
    {
        var satelliteService = new PythonSatelliteService();
        var earthSatellite = new EarthSatellite(
            "1 00694U 63047A   22330.85926710  .00001016  00000+0  12087-3 0  9995", 
            "2 00694  30.3573  13.8293 0579742  20.5362 341.7568 14.04095767962149");
        var observer = ICoordinateSystem3D<double>.Create(23.42, 52.11, 0);
        var start = new DateTimeOffset(2022, 12, 4, 19, 55, 11, TimeSpan.FromHours(-4));
        var interval = TimeSpan.FromSeconds(3);
        var degrees = 3;

        satelliteService.GetPolynomials(
            earthSatellite,
            observer,
            start,
            interval,
            degrees);
    }

    #endregion

}
