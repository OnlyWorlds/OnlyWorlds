using System;
using System.Collections.Generic;
[System.Serializable]
public class Institution : BaseElement
{
    // Foundation
    public string Premise;
    public int? FoundDate;
    public int? EndDate;
    public string ParentInstitutionId;
    // Claim
    public List<string> TerritoriesIds; = new List<string>();
    public List<string> ObjectsIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    public List<string> LegalIds; = new List<string>();
    // World
    public string Situation;
    public List<string> CooperatesIds; = new List<string>();
    public List<string> CompetitionIds; = new List<string>();
    public List<string> ConstructsIds; = new List<string>();
    public List<string> PhenomenaIds; = new List<string>();
}
