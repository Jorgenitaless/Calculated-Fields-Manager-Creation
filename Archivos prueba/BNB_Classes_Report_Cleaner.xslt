<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:wd="urn:com.workday.report/BNB_Classes_Info"
    exclude-result-prefixes="xsl wd xs xsi" version="3.0">
    <xsl:output method="text" encoding="UTF-8" />
    <xsl:template match="/">
        <xsl:text>BO,BO_WID,RBO,RBO_WID,Field,FieldID,FieldType&#10;</xsl:text>
        <xsl:apply-templates
            select="wd:Report_Data/wd:Report_Entry" />
    </xsl:template>
    <xsl:template match="wd:Report_Data/wd:Report_Entry">
        <xsl:variable name="BO" select="wd:Business_Object_Name" />
        <xsl:variable name="New_BO_WID"
            select="wd:Report_Fields[1]/wd:BO[@wd:Descriptor = $BO]/wd:ID" />
        <xsl:for-each select="wd:Report_Fields">
            <xsl:choose>
                <xsl:when
                    test="wd:RBO_WID = following::wd:Report_Fields/wd:RBO_WID"></xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select="$BO" />
                    <xsl:text>,</xsl:text>
                    <xsl:value-of select="$New_BO_WID" />
                    <xsl:text>,</xsl:text>
                    <xsl:value-of select="wd:RBO/@wd:Descriptor" />
                    <xsl:text>,</xsl:text>
                    <xsl:value-of select="wd:RBO/wd:ID" />
                    <xsl:text>,</xsl:text>
                    <xsl:value-of select="wd:Field/@wd:Descriptor" />
                    <xsl:text>,</xsl:text>
                    <xsl:value-of select="wd:Field/wd:ID" />
                    <xsl:text>,</xsl:text>
                    <xsl:value-of select="wd:fieldType" />
                    <xsl:text>&#10;</xsl:text>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>