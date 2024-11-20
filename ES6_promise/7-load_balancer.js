export default function loadBalancer(chinaDownload, USDownload) {
  // retourner la valeur de la première Promise résolue
  return Promise.race([chinaDownload, USDownload]);
}
