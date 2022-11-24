using NUnit.Framework;
using System.Threading.Tasks;

namespace Top50Satellites.SatelliteEngineAdapter.Tests;

internal class PythonEngineAdapterTests
{

    #region Properties and fields

    public static string PythonDllPath { get; } = @"C:\Program Files\Python311\python311.dll";

    #endregion

    #region Tests

    [Test]
    public async Task GetSatellites_ParseVisualTleDataFromFile_ReturnsExpectedTleDataCollection()
    {
        // ARRANGE
        PythonEngineAdapter engineAdapter = new PythonEngineAdapter(PythonDllPath);

        // ACT
        var result = await engineAdapter.GetSatellites(TestDataAccessor.TLEVisualPath);

        // ASSERT
        CollectionAssert.AreEqual(TestDataAccessor.TLEVisualParsed.Value, result);
    }

    #endregion

}