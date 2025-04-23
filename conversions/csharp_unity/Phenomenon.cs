using System;
using System.Collections.Generic;
[System.Serializable]
public class Phenomenon : BaseElement
{
    // Manifest
    public string Presence;
    public string Scope;
    public int? Duration;
    public string Intensity;
    public List<string> EmpowermentsIds; = new List<string>();
    public List<string> EnvironmentsIds; = new List<string>();
    public List<string> CarriersIds; = new List<string>();
    // Actuate
    public string Effect;
    public string CatalystsId;
    public List<string> WieldersIds; = new List<string>();
    public List<string> HandlersIds; = new List<string>();
    public List<string> EnablersIds; = new List<string>();
    public List<string> TriggersIds; = new List<string>();
    public List<string> AffinityIds; = new List<string>();
}
