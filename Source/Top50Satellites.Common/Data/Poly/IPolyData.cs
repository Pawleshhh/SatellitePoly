namespace Top50Satellites.Common;

public interface IPolyData : IEquatable<IPolyData>
{

    public IReadOnlyList<double> Coefficients { get; }

    public int Degrees { get; }

    public double Calculate(double x);

    public static IPolyData Create(IEnumerable<double> coefficients)
        => new PolyData(coefficients.ToArray());

}
