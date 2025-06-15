using System;
using System.Collections.Generic;
[System.Serializable]
public class Territory : BaseElement
{
    // Situation
    public string Terrain;
    public int? Size;
    public string ParentTerritoryId;
    // Yield
    public string Maintenance;
    public int? PrimaryOutput;
    public int? SecondaryOutput;
    public string PrimaryResourceId;
    public List<string> SecondaryResourcesIds; = new List<string>();
    // World
    public string History;
    public List<string> OccupantsIds; = new List<string>();
    public List<string> OccurrencesIds; = new List<string>();
}
