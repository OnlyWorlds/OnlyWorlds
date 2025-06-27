using System;
using System.Collections.Generic;
[System.Serializable]
public class Creature : BaseElement
{
    // Biology
    public string Appearance;
    public int? Weight;
    public int? Height;
    public List<string> SpeciesIds; = new List<string>();
    // Behaviour
    public string Habits;
    public string Demeanor;
    public List<string> TraitsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> LanguagesIds; = new List<string>();
    // World
    public string Status;
    public int? BirthDate;
    public string LocationId;
    public string ZoneId;
    // TTRPG
    public int? ChallengeRating;
    public int? HitPoints;
    public int? ArmorClass;
    public int? Speed;
    public List<string> ActionsIds; = new List<string>();
}
