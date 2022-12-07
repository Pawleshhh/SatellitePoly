namespace Top50Satellites.Common;

public interface ICoordinateSystem2D<T> : ICoordinateSystem<T>
    where T : struct, IEquatable<T>, IFormattable
{

    public T X { get; set; }
    public T Y { get; set; }

    public void Deconstruct(out T x, out T y)
    {
        x = X;
        y = Y;
    }

    public static ICoordinateSystem2D<T> Create(T x, T y)
    {
        return new CoordinateSystem2D<T>(x, y);
    }

}

record CoordinateSystem2D<T> : CoordinateSystem<T>, ICoordinateSystem2D<T>
    where T : struct, IEquatable<T>, IFormattable
{
    public T X { get => GetAxis(0); set => SetAxis(0, value); }
    public T Y { get => GetAxis(1); set => SetAxis(1, value); }

    public CoordinateSystem2D(T x, T y)
        : base(x, y) { }

    public bool Equals(ICoordinateSystem2D<T>? other)
    {
        if (other == null)
        {
            return false;
        }

        return X.Equals(other.X) && Y.Equals(other.Y);
    }
}