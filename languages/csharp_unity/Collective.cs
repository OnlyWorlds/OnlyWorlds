using System;
using System.Collections.Generic;
[System.Serializable]
public class Collective : BaseElement
{
    // Formation
    public string Composition;
    public int? Count;
    public int? FormationDate;
    public string OperatorId;
    public List<string> EquipmentIds; = new List<string>();
    // Dynamics
    public string Activity;
    public string Disposition;
    public string State;
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> SymbolismIds; = new List<string>();
    // World
    public List<string> SpeciesIds; = new List<string>();
    public List<string> CharactersIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    public List<string> PhenomenaIds; = new List<string>();
}
