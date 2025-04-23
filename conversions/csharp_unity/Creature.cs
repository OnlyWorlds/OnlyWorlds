using System;
using System.Collections.Generic;
[System.Serializable]
public class Creature : BaseElement
{
    // Physiology
    public string Appearance;
    public int? Weight;
    public int? Height;
    public List<string> SpeciesIds; = new List<string>();
    // Lifestyle
    public string Behaviour;
    public string Demeanour;
    public List<string> TraitsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> LanguagesIds; = new List<string>();
    // World
    public int? BirthDate;
    public string LocationId;
    public string TerritoryId;
    // Games
    public string Lore;
    public string Senses;
    public int? HitPoints;
    public int? ArmorClass;
    public int? ChallengeRating;
    public int? Speed;
    public int? TtStr;
    public int? TtInt;
    public int? TtCon;
    public int? TtDex;
    public int? TtWis;
    public int? TtCha;
    public List<string> ActionsIds; = new List<string>();
    public List<string> ReactionsIds; = new List<string>();
    public string Alignment;
}
