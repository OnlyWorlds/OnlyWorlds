using System;
using System.Collections.Generic;
[System.Serializable]
public class Character : BaseElement
{
    // Constitution
    public string Physicality;
    public string Psychology;
    public int? Height;
    public int? Weight;
    public List<string> SpeciesIds; = new List<string>();
    public List<string> TraitsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    // Origins
    public string Background;
    public string Motivations;
    public int? BirthDate;
    public string BirthplaceId;
    public List<string> LanguagesIds; = new List<string>();
    // World
    public string Situation;
    public string LocationId;
    public List<string> TitlesIds; = new List<string>();
    public List<string> ObjectsIds; = new List<string>();
    public List<string> InstitutionsIds; = new List<string>();
    // Personality
    public int? Charisma;
    public int? Coercion;
    public int? Capability;
    public int? Compassion;
    public int? Creativity;
    public int? Courage;
    // Social
    public List<string> FamilyIds; = new List<string>();
    public List<string> FriendsIds; = new List<string>();
    public List<string> RivalsIds; = new List<string>();
    // Games
    public string Backstory;
    public int? Level;
    public int? Power;
    public int? Price;
    public int? HitPoints;
    public int? SkillStealth;
    public int? TtStr;
    public int? TtInt;
    public int? TtCon;
    public int? TtDex;
    public int? TtWis;
    public int? TtCha;
    public string Class;
    public string Alignment;
    public List<string> EquipmentIds; = new List<string>();
    public List<string> BackpackIds; = new List<string>();
    public List<string> ProficienciesIds; = new List<string>();
    public List<string> FeaturesIds; = new List<string>();
    public List<string> SpellsIds; = new List<string>();
    public List<string> InspirationsIds; = new List<string>();
}
