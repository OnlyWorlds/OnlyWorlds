using System;
using System.Collections.Generic;
[System.Serializable]
public class Family : BaseElement
{
    // Community
    public string Spirit;
    public List<string> AlliancesIds; = new List<string>();
    public List<string> RivalriesIds; = new List<string>();
    // Lineage
    public string History;
    public List<string> AncestorsIds; = new List<string>();
    public List<string> TraitsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> LanguagesIds; = new List<string>();
    // World
    public string Status;
    public List<string> CompetitionIds; = new List<string>();
    public List<string> AdministratesIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    // Legacy
    public string Traditions;
    public string EstateId;
    public List<string> HeirloomsIds; = new List<string>();
}
