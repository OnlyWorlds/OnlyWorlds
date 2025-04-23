using System;
using System.Collections.Generic;
[System.Serializable]
public class Relation : BaseElement
{
    // Nature
    public string History;
    public string Impact;
    public int? StartDate;
    public int? EndDate;
    public int? Debt;
    public List<string> EventsIds; = new List<string>();
    // Involves
    public string PrimaryCharacterId;
    public string PrimaryCreatureId;
    public string PrimaryInstitutionId;
    public List<string> SecondaryCharactersIds; = new List<string>();
    public List<string> SecondaryCreaturesIds; = new List<string>();
    public List<string> SecondaryInstitutionsIds; = new List<string>();
}
