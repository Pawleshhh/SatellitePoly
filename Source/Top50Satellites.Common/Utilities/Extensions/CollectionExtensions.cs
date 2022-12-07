namespace Top50Satellites.Common;

public static class CollectionExtensions
{

    #region IEnumerable

    public static bool IsNullOrEmpty<T>(this IEnumerable<T> @this)
        => @this == null || !@this.Any();

    public static void ForEach<T>(this IEnumerable<T> @this, Action<T> action)
    {
        foreach(var item in @this)
        {
            action(item);
        }
    }

    #endregion

}
