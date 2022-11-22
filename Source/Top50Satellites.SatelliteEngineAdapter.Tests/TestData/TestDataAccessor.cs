using System;
using System.Collections.Generic;
using static Top50Satellites.Common.ResourceHelper;

namespace Top50Satellites.SatelliteEngineAdapter.Tests;

internal class TestDataAccessor
{
    public static Lazy<string> TLEVisual { get; } = new Lazy<string>(() => ReadResource<TestDataAccessor>("Top50Satellites.Tests.TestData.visual.txt"), true);
    public static Lazy<string> TLENoaa { get; } = new Lazy<string>(() => ReadResource<TestDataAccessor>("Top50Satellites.Tests.TestData.noaa.txt"), true);
    public static Lazy<string> TLEGnss { get; } = new Lazy<string>(() => ReadResource<TestDataAccessor>("Top50Satellites.Tests.TestData.gnss.txt"), true);

    public static Dictionary<string, Lazy<string>> TleDataByName = new()
    {
        ["visual"] = TLEVisual,
        ["noaa"] = TLENoaa,
        ["gnss"] = TLEGnss
    };

}
