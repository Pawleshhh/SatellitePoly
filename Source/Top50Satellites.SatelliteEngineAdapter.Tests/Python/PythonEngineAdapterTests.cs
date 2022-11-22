using NUnit.Framework;
using System.IO;
using System.Threading.Tasks;

namespace Top50Satellites.SatelliteEngineAdapter.Tests;

internal class PythonEngineAdapterTests
{

    #region Tests

    [Test]
    public async Task GetSatellites_Test()
    {
        PythonEngineAdapter engineAdapter = new PythonEngineAdapter(@"C:\Program Files\Python311\python311.dll");

        var result = await engineAdapter.GetSatellites(
            @"D:\Programming\Top50Satellites\Source\Top50Satellites.SatelliteEngineAdapter.Tests\TestData\visual.txt");
    }

    #endregion

}