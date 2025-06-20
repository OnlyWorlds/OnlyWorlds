using System;
using System.Collections.Generic;
[System.Serializable]
public class Object : BaseElement
{
    // Form
    public string Aesthetics;
    public int? Weight;
    public int? Amount;
    public string ParentObjectId;
    public List<string> MaterialsIds; = new List<string>();
    public List<string> TechnologyIds; = new List<string>();
    // Function
    public string Utility;
    public List<string> EffectsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> ConsumesIds; = new List<string>();
    // World
    public string Origins;
    public string LocationId;
    public string LanguageId;
    public List<string> AffinitiesIds; = new List<string>();
}
