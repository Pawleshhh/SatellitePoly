namespace Top50Satellites.Common;

public interface ICoordinateSystem3D<T> : ICoordinateSystem<T>
    where T : struct, IEquatable<T>, IFormattable
{

    public T X { get; set; }
    public T Y { get; set; }
    public T Z { get; set; }

    public void Deconstruct(out T x, out T y)
    {
        x = X;
        y = Y;
    }

    public void Deconstruct(out T x, out T y, out T z)
    {
        x = X;
        y = Y;
        z = Z;
    }

    public static ICoordinateSystem3D<T> Create(T x, T y, T z)
    {
        return new CoordinateSystem3D<T>(x, y, z);
    }

}

record CoordinateSystem3D<T> : CoordinateSystem<T>, ICoordinateSystem3D<T>
    where T : struct, IEquatable<T>, IFormattable
{
    public T X { get => GetAxis(0); set => SetAxis(0, value); }
    public T Y { get => GetAxis(1); set => SetAxis(1, value); }
    public T Z { get => GetAxis(2); set => SetAxis(2, value); }

    public CoordinateSystem3D(T x, T y, T z)
        : base(x, y, z) { }

    public bool Equals(ICoordinateSystem3D<T>? other)
    {
        if (other == null)
        {
            return false;
        }

        return X.Equals(other.X)
            && Y.Equals(other.Y)
            && Z.Equals(other.Z);
    }
}