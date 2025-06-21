using System;
using System.Collections.Generic;
[System.Serializable]
public class Construct : BaseElement
{
    // Nature
    public string Rationale;
    public string History;
    public string Status;
    public string Reach;
    public int? StartDate;
    public int? EndDate;
    public string FounderId;
    public string CustodianId;
    // Involves
    public List<string> CharactersIds; = new List<string>();
    public List<string> ObjectsIds; = new List<string>();
    public List<string> LocationsIds; = new List<string>();
    public List<string> SpeciesIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    public List<string> InstitutionsIds; = new List<string>();
    public List<string> TraitsIds; = new List<string>();
    public List<string> CollectivesIds; = new List<string>();
    public List<string> ZonesIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> PhenomenaIds; = new List<string>();
    public List<string> LanguagesIds; = new List<string>();
    public List<string> FamiliesIds; = new List<string>();
    public List<string> RelationsIds; = new List<string>();
    public List<string> TitlesIds; = new List<string>();
    public List<string> ConstructsIds; = new List<string>();
    public List<string> EventsIds; = new List<string>();
    public List<string> NarrativesIds; = new List<string>();
}
