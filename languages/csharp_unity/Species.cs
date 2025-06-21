using System;
using System.Collections.Generic;
[System.Serializable]
public class Species : BaseElement
{
    // Biology
    public string Appearance;
    public int? LifeSpan;
    public int? TypicalWeight;
    public List<string> DietIds; = new List<string>();
    public List<string> ReproductionIds; = new List<string>();
    // Psychology
    public string Instincts;
    public string Sociality;
    public string Temperament;
    public string Communication;
    public int? Aggression;
    public List<string> TraitsIds; = new List<string>();
    // World
    public string Role;
    public string ParentSpeciesId;
    public List<string> LocationsIds; = new List<string>();
    public List<string> ZonesIds; = new List<string>();
    public List<string> AffinitiesIds; = new List<string>();
}
