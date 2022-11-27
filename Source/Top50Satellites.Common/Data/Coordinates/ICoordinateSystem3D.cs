namespace Top50Satellites.Common;

public interface ICoordinateSystem3D<T> : ICoordinateSystem
    where T : struct, IEquatable<T>, IFormattable
{

    public T X { get; }
    public T Y { get; }
    public T Z { get; }

    void Deconstruct(out T x, out T y, out T z)
    {
        x = X;
        y = Y;
        z = Z;
    }

    public static ICoordinateSystem3D<T> Create(T x, T y, T z)
        => new CoordinateSystem3D<T>(x, y, z);

}

internal record CoordinateSystem3D<T> : CoordinateSystem<T>, ICoordinateSystem3D<T>
    where T : struct, IEquatable<T>, IFormattable
{

    public T X => GetAt(0);

    public T Y => GetAt(1);

    public T Z => GetAt(2);

    public CoordinateSystem3D(T x, T y, T z)
        : base(x, y, z)
    {

    }

}