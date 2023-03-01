<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:wd="urn:com.workday.report/BNB_Classes_Info"
    exclude-result-prefixes="xsl wd xs xsi" version="3.0">
    <xsl:template match="/">
        <Root>
            <xsl:apply-templates select="wd:Report_Data" />
        </Root>
    </xsl:template>
    <xsl:template match="wd:Report_Data/wd:Report_Entry">
        <Row>
            <xsl:variable name="BO" select="wd:Business_Object_Name" />
            <xsl:variable name="New_BO_WID"
                select="wd:Report_Fields[1]/wd:BO[@wd:Descriptor = $BO]/wd:ID" />
            <xsl:for-each select="wd:Report_Fields">
                <xsl:choose>
                    <xsl:when
                        test="wd:RBO_WID = following::wd:Report_Fields/wd:RBO_WID">
                    </xsl:when>
                    <xsl:otherwise>
                        <Relation>
                            <Field>
                                <xsl:value-of select="wd:Field/@wd:Descriptor" />
                            </Field>
                            <FieldID>
                                <xsl:value-of select="wd:Field_WID" />
                            </FieldID>
                            <BO>
                                <xsl:value-of select="$BO" />
                            </BO>
                            <BO_WID>
                                <xsl:value-of select="$New_BO_WID" />
                                <!-- <xsl:value-of select="$New_BO_WID" /> -->
                            </BO_WID>
                            <RBO>
                                <xsl:value-of select="wd:RBO/@wd:Descriptor" />
                            </RBO>
                            <RBO_WID>
                                <xsl:value-of select="wd:RBO_WID" />
                            </RBO_WID>
                            <fieldType>
                                <xsl:value-of select="wd:fieldType" />
                            </fieldType>
                        </Relation>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
        </Row>
    </xsl:template>
</xsl:stylesheet>