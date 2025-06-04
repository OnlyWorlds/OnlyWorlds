using System;
using System.Collections.Generic;
[System.Serializable]
public class Ability : BaseElement
{
    // Mechanics
    public string Usage;
    public int? Range;
    public int? Strength;
    public List<string> EffectsIds; = new List<string>();
    public List<string> UtilityIds; = new List<string>();
    // Dynamics
    public string Difficulty;
    public List<string> TalentIds; = new List<string>();
    public List<string> EnablersIds; = new List<string>();
    public List<string> RequirementsIds; = new List<string>();
    // World
    public string Prevalence;
    public string SystemId;
    public string ConstructId;
}
