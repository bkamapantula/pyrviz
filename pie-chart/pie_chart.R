library(ggplot2)

# define data
y_data <- c(3417, 3079, 873, 803, 355, 187, 160, 113, 12)
y_labels <- c("PubMeds", "Validated \nTargets", "Functions", "miRNAs", "Pathways", "Regulators", "Diseases", "Chemicals", "Species")

# create dataframe 
df <- data.frame(cbind(y_data, y_labels))

# converts strings to numbers
df$y_data <- as.numeric(as.character(df$y_data))
df$y_labels <- as.character(df$y_labels)

# coord_polar for pie chart
plt <- ggplot(df, aes(x=1, y=y_data, fill=y_labels)) +
		ggtitle("Distribution of Species data") +
		coord_polar(theta='y') 
        #+ scale_y_discrete(breaks=NULL, labels=NULL) #df$y_labels)

# add layer and remove legend
plt <- plt + geom_bar(stat="identity", color="black") +
		guides(fill=FALSE)

plt <- plt + theme(
	axis.ticks=element_blank(), # removes ticks
	axis.title=element_blank(), # removes y axis label
	axis.text.y=element_blank()) # removes 0.75, 1.00, 1.25 labels

wedge_breaks <- cumsum(df$y_data) - df$y_data/2
print(wedge_breaks)

plt <- plt + 
		# black labels
		theme(axis.text.x=element_text(color='black')) +
        scale_y_discrete(
            breaks=wedge_breaks, 
            labels=df$y_labels
        )

print(plt)
