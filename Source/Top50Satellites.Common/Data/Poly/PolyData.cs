using System.Text;

namespace Top50Satellites.Common;

internal class PolyData : IPolyData
{

    #region Fields

    private readonly double[] coefficients;
    private string? thisAsString = null;

    #endregion

    #region Constructors

    public PolyData(params double[] coefficients)
    {
        if (coefficients.IsNullOrEmpty())
        {
            throw new ArgumentException(nameof(coefficients));
        }

        this.coefficients = coefficients;
    }

    #endregion

    #region Properties

    public IReadOnlyList<double> Coefficients => this.coefficients;

    public int Degrees => this.coefficients.Length - 1;

    #endregion

    #region Methods

    public double Calculate(double x)
    {
        double result = 0.0;
        for(int i = 0; i < this.coefficients.Length; i++)
        {
            var coefficient = this.coefficients[i];
            result += coefficient * Math.Pow(x, i);
        }

        return result;
    }

    public bool Equals(IPolyData? other)
    {
        if (other == null)
        {
            return false;
        }

        if (this.coefficients.Length != other.Coefficients.Count)
        {
            return false;
        }

        for(int i = 0; i < this.coefficients.Length; i++)
        {
            if (this.coefficients[i] != other.Coefficients[i])
            {
                return false;
            }
        }

        return true;
    }

    public override bool Equals(object? obj)
    {
        if (obj is IPolyData polyData)
        {
            return Equals(polyData);
        }

        return false;
    }

    public override int GetHashCode()
    {
        int hash = 0;
        this.coefficients.ForEach(x => hash += x.GetHashCode() * 17);
        return hash;
    }

    public override string ToString()
    {
        if (this.thisAsString == null)
        {
            StringBuilder stringBuilder = new("[ ");
            foreach (var coefficient in this.coefficients)
            {
                stringBuilder.Append($"{coefficient} ");
            }
            stringBuilder.Append("]");

            this.thisAsString = stringBuilder.ToString();
        }

        return this.thisAsString;
    }

    #endregion

}
