using System;
[System.Serializable]
public class Title : BaseElement
{
    // Nature
    public string Privileges;
    public string Conditions;
    public int? CreateDate;
    public int? AssignDate;
    public int? RevokeDate;
    public int? Hierarchy;
    // Issue
    public string Rights;
    public string AuthorId;
    // World
    public string CharacterId;
    public string LocationId;
    public string ObjectId;
    public string InstitutionId;
    public string CreatureId;
    public string ZoneId;
    public string CollectiveId;
    public string ConstructId;
}
