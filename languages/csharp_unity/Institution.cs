using System;
using System.Collections.Generic;
[System.Serializable]
public class Institution : BaseElement
{
    // Foundation
    public string Doctrine;
    public int? FoundingDate;
    public string ParentInstitutionId;
    // Claims
    public List<string> LegislationIds; = new List<string>();
    public List<string> ZonesIds; = new List<string>();
    public List<string> ObjectsIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    // World
    public string Status;
    public List<string> AlliesIds; = new List<string>();
    public List<string> AdversariesIds; = new List<string>();
    public List<string> ConstructsIds; = new List<string>();
}
