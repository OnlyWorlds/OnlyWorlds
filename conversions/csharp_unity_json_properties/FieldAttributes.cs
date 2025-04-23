// Defines custom attributes used to provide metadata for data model fields.
// These attributes can be used by serializers (like Newtonsoft.Json via JsonProperty),
// custom editor tooling (e.g., UIToolkit inspectors), and validation logic.
    
public class TextAttribute : Attribute
{
    public string Value { get; private set; }

    public TextAttribute(string value)
    {
        Value = value;
    }
}


public class IntegerAttribute : Attribute
{
    public int MaxValue { get; private set; }

    public IntegerAttribute(int maxValue = 0)
    {
        MaxValue = maxValue;
    }
}

public class ReferenceAttribute : Attribute
{
    public Type ReferenceType { get; private set; }
    public bool AllowMultiple { get; private set; }
    public string ConstrainedSupertype { get; private set; }
    public string ConstrainedSubtype { get; private set; }

    public ReferenceAttribute(Type referenceType, bool allowMultiple = false, string constrainedSupertype = "",   string constrainedSubtype = "")
    {
        ReferenceType = referenceType;
        AllowMultiple = allowMultiple;
        ConstrainedSupertype = constrainedSupertype;
        ConstrainedSubtype = constrainedSubtype;
    }
} 
public class ReverseLookupAttribute : Attribute
{
    public Type ReferenceType { get; private set; } 
    public string ReferenceField  { get; private set; } 

    public ReverseLookupAttribute(Type referenceType, string referenceField )
    {
        ReferenceType = referenceType;
        ReferenceField = referenceField;
    }
} 
 