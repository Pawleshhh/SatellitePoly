namespace Top50Satellites.Common;


public interface ICoordinateSystem
{

    public int AxisCount { get; }

    public object this[int index] { get; }

    public object GetAt(int axisIndex);

}

public record CoordinateSystem<T> : ICoordinateSystem
    where T : struct, IEquatable<T>, IFormattable
{

    #region Fields

    private readonly T[] axes;

    #endregion

    #region Constructors

    public CoordinateSystem(params T[] axes)
    {
        this.axes = axes ?? throw new ArgumentNullException(nameof(axes));
    }

    #endregion

    #region Properties

    public T this[int index] => GetAt(index);

    object ICoordinateSystem.this[int index] => GetAt(index);

    public int AxisCount => axes.Length;

    #endregion

    #region Methods

    public T GetAt(int axisIndex)
    {
        return axes[axisIndex];
    }

    object ICoordinateSystem.GetAt(int axisIndex)
    {
        return GetAt(axisIndex);
    }

    #endregion

}
