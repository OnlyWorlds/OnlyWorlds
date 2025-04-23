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
    public List<string> TechnologyIds; = new List<string>();
    // Function
    public string Utility;
    public List<string> EffectsIds; = new List<string>();
    public List<string> EnablesIds; = new List<string>();
    public List<string> ConsumesIds; = new List<string>();
    // World
    public string Origins;
    public string LocationId;
    // Games
    public string Craftsmanship;
    public string Requirements;
    public string Durability;
    public int? Value;
    public int? Damage;
    public int? Armor;
    public string Rarity;
    public string LanguageId;
    public List<string> RequiresIds; = new List<string>();
}
