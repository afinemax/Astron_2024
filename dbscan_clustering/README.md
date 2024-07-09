## Maxwell Fine Jul 9 2024

<table>
  <tr>
    <td style="text-align: center;">
      <img src="https://github.com/afinemax/Astron_2024/blob/main/dbscan_clustering/DBscan_clustering_final_v1.png" alt="Resulting Plot" width="500">
    </td>
    <td style="text-align: center;">
      <img src="https://github.com/afinemax/Astron_2024/blob/main/dbscan_clustering/DBscan_clustering_final_v1_zoom.png" alt="Zoom in on Resulting plot" width="500">
    </td>
  </tr>
</table>


### This notebook is for 1) trying out DBscan, and 2) using DBscan to cluster candidate signals from `presto`

Clustering is done between `DM` and `time`. RFI, and Real signals are picked up as mulitple candidates in both time, and DM, with little seperation. Signals that are bright will trigger in multiple DMs but still be relatively isolated in time. 


### dbscan has two arguments:
- eps (ε): The maximum distance between two samples for one to be considered as in the neighborhood of the other. This is not a maximum bound on the distances of points within a cluster. This is the most important DBSCAN parameter to choose appropriately for your data set and distance function.
- min_samples: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself. If `min_samples` is set to a higher value, DBSCAN will find denser clusters, whereas if it is set to a lower value, the found clusters will be more sparse.

### Note:
- There is only one eps parameters, as opposed to n for n dimensions. In higher dimensions, we typically want to cluster paremters with - different units. To do this we must `rescale` the dimensions so that they are comparable.
- each candidate file has a time width of 40ms, so clusters should not have a temporal width of 40ms>  


### Idea:
- We know that temporally (time), bursts have a width of ~1ms or 1/1000 of a second, we can try to force rescale DM so that the spacing between each DM sample is ~1/1000 of a DM unit pc/cm^3. This should let us cluster the same signals together as the burst duration and sepeartion in DM would then be comparable.
- min_samples = 3, we expect a signal to be at the real DM, and one +/- the real DM


### Suggestion For Future Improvement:
- take into account simga for clustering in 3D



