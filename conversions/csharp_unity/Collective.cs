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
    // Agency
    public string Activity;
    public string Temperance;
    public List<string> SkillsIds; = new List<string>();
    public List<string> RitualsIds; = new List<string>();
    // World
    public List<string> SpeciesIds; = new List<string>();
    public List<string> CharactersIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
    public List<string> PhenomenaIds; = new List<string>();
}
