using System.Collections;

namespace Top50Satellites.Common;

public interface ICoordinateSystem<T> : IEquatable<ICoordinateSystem<T>>, IEnumerable<T>
    where T : struct, IEquatable<T>, IFormattable
{
    int AxesCount { get; }

    T GetAxis(int axis);
    void SetAxis(int axis, T value);

}

internal record CoordinateSystem<T> : ICoordinateSystem<T>
    where T : struct, IEquatable<T>, IFormattable
{

    #region Fields

    private readonly T[] axes;

    #endregion

    #region Properties

    public int AxesCount => axes.Length;

    #endregion

    #region Constructors

    public CoordinateSystem(IEnumerable<T> points)
    {
        if (points == null)
        {
            throw new ArgumentNullException(nameof(points));
        }

        axes = points.ToArray();
    }

    public CoordinateSystem(params T[] points)
        : this((IEnumerable<T>)points)
    {

    }

    #endregion

    #region Methods

    public T GetAxis(int axis)
    {
        return axes[axis];
    }

    public void SetAxis(int axis, T value)
    {
        axes[axis] = value;
    }

    public virtual bool Equals(ICoordinateSystem<T>? other)
    {
        if (other == null || AxesCount != other.AxesCount)
        {
            return false;
        }

        for (int i = 0; i < AxesCount; i++)
        {
            if (!axes[i].Equals(other.GetAxis(i)))
            {
                return false;
            }
        }

        return true;
    }

    public override int GetHashCode()
    {
        int hashCode = 0;

        foreach (var axis in axes)
        {
            hashCode ^= axis.GetHashCode() * 17;
        }

        return hashCode;
    }

    public override string ToString()
    {
        return string.Join(',', axes);
    }

    public IEnumerator<T> GetEnumerator()
    {
        return ((IEnumerable<T>)axes).GetEnumerator();
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    #endregion

}
