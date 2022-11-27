namespace Top50Satellites.Common;

public interface ICoordinateSystem2D<T> : ICoordinateSystem
    where T : struct, IEquatable<T>, IFormattable
{

    public T X { get; }
    public T Y { get; }

    void Deconstruct(out T x, out T y)
    {
        x = X;
        y = Y;
    }

    public static ICoordinateSystem2D<T> Create(T x, T y)
        => new CoordinateSystem2D<T>(x, y);

}

internal record CoordinateSystem2D<T> : CoordinateSystem<T>, ICoordinateSystem2D<T>
    where T : struct, IEquatable<T>, IFormattable
{

    public T X => GetAt(0);

    public T Y => GetAt(1);

    public CoordinateSystem2D(T x, T y)
        : base(x, y)
    {

    }

}
