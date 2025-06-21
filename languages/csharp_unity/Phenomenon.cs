using System;
using System.Collections.Generic;
[System.Serializable]
public class Phenomenon : BaseElement
{
    // Mechanics
    public string Expression;
    public string Effects;
    public int? Duration;
    public List<string> CatalystsIds; = new List<string>();
    public List<string> EmpowermentsIds; = new List<string>();
    // World
    public string Mythology;
    public string SystemId;
    public List<string> TriggersIds; = new List<string>();
    public List<string> WieldersIds; = new List<string>();
    public List<string> EnvironmentsIds; = new List<string>();
}
