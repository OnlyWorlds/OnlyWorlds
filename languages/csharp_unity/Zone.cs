using System;
using System.Collections.Generic;
[System.Serializable]
public class Zone : BaseElement
{
    // Scope
    public string Role;
    public int? StartDate;
    public int? EndDate;
    public List<string> PhenomenaIds; = new List<string>();
    public List<string> LinkedZonesIds; = new List<string>();
    // World
    public string Context;
    public List<string> PopulationsIds; = new List<string>();
    public List<string> TitlesIds; = new List<string>();
    public List<string> PrinciplesIds; = new List<string>();
}
