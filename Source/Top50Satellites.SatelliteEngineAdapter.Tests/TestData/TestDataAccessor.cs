using System;
using System.Collections.Generic;
using static Top50Satellites.Common.ResourceHelper;

namespace Top50Satellites.SatelliteEngineAdapter.Tests;

internal class TestDataAccessor
{
    public static Lazy<string> TLEVisual { get; } = new Lazy<string>(() => ReadResource<TestDataAccessor>("Top50Satellites.Tests.TestData.visual.txt"), true);
    public static Lazy<string> TLENoaa { get; } = new Lazy<string>(() => ReadResource<TestDataAccessor>("Top50Satellites.Tests.TestData.noaa.txt"), true);
    public static Lazy<string> TLEGnss { get; } = new Lazy<string>(() => ReadResource<TestDataAccessor>("Top50Satellites.Tests.TestData.gnss.txt"), true);

    public static string TLEVisualPath { get; } = GetAssemblyPath<TestDataAccessor>() + @"\TestData\visual.txt";
    public static string TLENoaaPath { get; } = GetAssemblyPath<TestDataAccessor>() + @"\TestData\noaa.txt";
    public static string TLEGnssPath { get; } = GetAssemblyPath<TestDataAccessor>() + @"\TestData\gnss.txt";

    public static Lazy<IEnumerable<TleData>> TLEVisualParsed { get; } = new Lazy<IEnumerable<TleData>>(() => new TleData[]
    {
        new(2459888.0334955659, "ATLAS CENTAUR 2", 694, "U", "63047A", 22, 308.5334957, 2459887.5, 9.7962664439195608E-11, 0, 
            0.00040661, 0, 999, 0.52980167575988668, 2.3917293937629496, 0.0580081, 3.2508101221918424, 
            3.0203114691979591, 0.0612617591091252, 95938),
        new(2459887.9420134667, "THOR AGENA D R/B", 733, "U", "64002A", 22, 308.4420136, 2459887.5, 1.151432492635148E-11, 0,
            0.00015642, 0, 999, 1.7278305809138343, 4.2379404218518033, 0.0032962, 3.7343989700174234,
            2.5471684169455644, 0.062509019083722153, 6379),
        new(2459887.8487024475, "SL-3 R/B", 877, "U", "64053B", 22, 308.34870258, 2459887.5, 1.075680354961783E-11, 0,
            9.7832000000000008E-05, 0, 999, 1.1358131533081057, 5.3508740539955149, 0.0052266, 0.84647945122949375,
            5.4464221038959453, 0.0636874553153923, 8843),
        new(2459887.9216915569, "SL-8 R/B", 2802, "U", "67045B", 22, 308.42169169, 2459887.5, 1.4847418983979539E-11, 0,
            0.00014753, 0, 999, 1.2917286513765152, 1.8458532355921951, 0.0065579, 0.81373183847432418, 
            5.4809586791344085, 0.063005806154984551, 91268),
        new(2459887.807219198, "SL-8 R/B", 3230, "U", "68040B", 22, 308.30721933, 2459887.5, 1.0805284917728784E-10, 0,
            0.00035423, 0, 999, 1.2921580023725059, 4.6292589481122, 0.002812, 0.89106563230094094, 
            5.3985459771844884, 0.065093411839321019, 90723)
    });

}
