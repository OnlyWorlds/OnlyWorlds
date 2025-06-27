using System;
using System.Collections.Generic;
[System.Serializable]
public class Title : BaseElement
{
    // Mandate
    public string Authority;
    public string Eligibility;
    public int? GrantDate;
    public int? RevokeDate;
    public string IssuerId;
    public string BodyId;
    public string SuperiorTitleId;
    public List<string> HoldersIds; = new List<string>();
    public List<string> SymbolsIds; = new List<string>();
    // World
    public string Status;
    public string History;
    public List<string> CharactersIds; = new List<string>();
    public List<string> InstitutionsIds; = new List<string>();
    public List<string> FamiliesIds; = new List<string>();
    public List<string> ZonesIds; = new List<string>();
    public List<string> LocationsIds; = new List<string>();
    public List<string> ObjectsIds; = new List<string>();
    public List<string> ConstructsIds; = new List<string>();
    public List<string> LawsIds; = new List<string>();
    public List<string> CollectivesIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    public List<string> PhenomenaIds; = new List<string>();
    public List<string> SpeciesIds; = new List<string>();
    public List<string> LanguagesIds; = new List<string>();
}
