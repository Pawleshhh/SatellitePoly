using NUnit.Framework;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace Top50Satellites.SatelliteEngineAdapter.Tests;

internal class PythonEngineAdapterTests
{

    #region Properties and fields

    public static string PythonDllPath { get; } = @"C:\Program Files\Python311\python311.dll";

    public static Func<PythonEngineAdapter> PythonEngine { get; } = () => new PythonEngineAdapter();

    #endregion

    #region SetUp and TearDown

    [OneTimeSetUp]
    public void OneTimeSetUp()
    {
        PythonEngineAdapter.InitializeEngine(PythonDllPath);
    }

    #endregion

    #region Tests

    [Test]
    public async Task GetSatellites_ParseVisualTleDataFromFile_ReturnsExpectedTleDataCollection()
    {
        // ARRANGE
        var pythonEngine = PythonEngine();

        // ACT
        var result = await pythonEngine.GetSatellites(TestDataAccessor.TLEVisualPath);

        // ASSERT
        CollectionAssert.AreEqual(TestDataAccessor.TLEVisualParsed.Value, result);
    }

    [Test]
    public async Task GetSatelliteDataAge_CompareSatelliteAge_ReturnsExpectedComparisonResult()
    {
        // ARRANGE
        var pythonEngine = PythonEngine();
        var dateTime = new DateTime(2022, 11, 24);
        var tleData = TestDataAccessor.TLEVisualParsed.Value.First();
        var expected = TimeSpan.FromDays(19.467305174864375);

        // ACT
        var result = await pythonEngine.GetSatelliteDataAge(
            dateTime,
            tleData);

        // ASSERT
        Assert.AreEqual(expected, result);
    }

    #endregion

}