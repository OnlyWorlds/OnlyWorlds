using System;
using System.Collections.Generic;
[System.Serializable]
public class Zone : BaseElement
{
    // Scope
    public string Function;
    public int? StartDate;
    public int? EndDate;
    public List<string> PhenomenaIds; = new List<string>();
    // World
    public string History;
    public List<string> ClaimedByIds; = new List<string>();
    public List<string> RoamedByIds; = new List<string>();
    public List<string> TitlesIds; = new List<string>();
}
