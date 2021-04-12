-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 13, 2021 at 01:28 AM
-- Server version: 8.0.23-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jaya_abadi`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `barang_id` varchar(10) NOT NULL,
  `barang_nama` varchar(100) NOT NULL,
  `barang_kategori` varchar(10) NOT NULL,
  `barang_merek` varchar(10) NOT NULL,
  `barang_varian` varchar(100) NOT NULL,
  `barang_satuan_grosir` varchar(10) NOT NULL,
  `barang_satuan_eceran` varchar(10) NOT NULL,
  `barang_harga_jual` int NOT NULL,
  `barang_harga_beli` int NOT NULL,
  `barang_stok_toko` int NOT NULL DEFAULT '0',
  `barang_stok_gudang` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`barang_id`, `barang_nama`, `barang_kategori`, `barang_merek`, `barang_varian`, `barang_satuan_grosir`, `barang_satuan_eceran`, `barang_harga_jual`, `barang_harga_beli`, `barang_stok_toko`, `barang_stok_gudang`) VALUES
('B4127279', 'PAKU', 'K624024', 'M34031', '1CM', 'S74773', 'S74773', 200, 100, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `kategori`
--

CREATE TABLE `kategori` (
  `kategori_id` varchar(10) NOT NULL,
  `kategori_nama` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `kategori`
--

INSERT INTO `kategori` (`kategori_id`, `kategori_nama`) VALUES
('K624024', 'SANGAT UMUM');

-- --------------------------------------------------------

--
-- Table structure for table `master_pelanggan`
--

CREATE TABLE `master_pelanggan` (
  `pelanggan_id` varchar(10) NOT NULL,
  `pelanggan_nama` varchar(100) NOT NULL,
  `pelanggan_alamat` varchar(100) NOT NULL,
  `pelanggan_kontak` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `master_pelanggan`
--

INSERT INTO `master_pelanggan` (`pelanggan_id`, `pelanggan_nama`, `pelanggan_alamat`, `pelanggan_kontak`) VALUES
('PEL6424533', 'JEFRI', 'jl manguni', '088101010');

-- --------------------------------------------------------

--
-- Table structure for table `master_supplier`
--

CREATE TABLE `master_supplier` (
  `supplier_id` varchar(20) NOT NULL,
  `supplier_nama` varchar(100) NOT NULL,
  `supplier_alamat` varchar(100) NOT NULL,
  `supplier_provinsi` varchar(100) NOT NULL,
  `supplier_kota` varchar(100) NOT NULL,
  `supplier_telepon` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `master_supplier`
--

INSERT INTO `master_supplier` (`supplier_id`, `supplier_nama`, `supplier_alamat`, `supplier_provinsi`, `supplier_kota`, `supplier_telepon`) VALUES
('SUP3395801', 'MUNDUR SENDIRI', 'jl 14 februari no banyak', 'Sulawesi Utara', 'Tomohon', '088819232323'),
('SUP4385565', 'MAJU BERSAMA', 'jl. manguni no 102', 'Sulawesi Utara', 'Manado', '088991919');

-- --------------------------------------------------------

--
-- Table structure for table `merek`
--

CREATE TABLE `merek` (
  `merek_id` varchar(10) NOT NULL,
  `merek_nama` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `merek`
--

INSERT INTO `merek` (`merek_id`, `merek_nama`) VALUES
('M34031', 'UMUM');

-- --------------------------------------------------------

--
-- Table structure for table `pembelian`
--

CREATE TABLE `pembelian` (
  `pembelian_id` varchar(100) NOT NULL,
  `pembelian_supplier_id` varchar(100) NOT NULL,
  `pembelian_tanggal` varchar(10) NOT NULL,
  `pembelian_jatuh_tempo` varchar(10) NOT NULL,
  `pembelian_faktur` varchar(100) NOT NULL,
  `pembelian_pajak` int NOT NULL,
  `pembelian_diskon` int NOT NULL,
  `pembelian_total` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `pengguna_id` varchar(10) NOT NULL,
  `pengguna_nama` varchar(100) NOT NULL,
  `pengguna_posisi` int NOT NULL,
  `pengguna_status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`pengguna_id`, `pengguna_nama`, `pengguna_posisi`, `pengguna_status`) VALUES
('USR79539', 'JOHN DOE', 1001, 1);

-- --------------------------------------------------------

--
-- Table structure for table `posisi`
--

CREATE TABLE `posisi` (
  `posisi_id` int NOT NULL,
  `posisi_nama` varchar(20) NOT NULL,
  `posisi_level` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `posisi`
--

INSERT INTO `posisi` (`posisi_id`, `posisi_nama`, `posisi_level`) VALUES
(1001, 'Administrator', 0),
(2001, 'Kasir', 1),
(3001, 'Sales', 2);

-- --------------------------------------------------------

--
-- Table structure for table `satuan`
--

CREATE TABLE `satuan` (
  `satuan_id` varchar(10) NOT NULL,
  `satuan_nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `satuan`
--

INSERT INTO `satuan` (`satuan_id`, `satuan_nama`) VALUES
('S22180', 'ROL'),
('S74773', 'METER');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`barang_id`);

--
-- Indexes for table `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`kategori_id`);

--
-- Indexes for table `master_pelanggan`
--
ALTER TABLE `master_pelanggan`
  ADD PRIMARY KEY (`pelanggan_id`);

--
-- Indexes for table `master_supplier`
--
ALTER TABLE `master_supplier`
  ADD PRIMARY KEY (`supplier_id`);

--
-- Indexes for table `merek`
--
ALTER TABLE `merek`
  ADD PRIMARY KEY (`merek_id`);

--
-- Indexes for table `pembelian`
--
ALTER TABLE `pembelian`
  ADD PRIMARY KEY (`pembelian_id`);

--
-- Indexes for table `posisi`
--
ALTER TABLE `posisi`
  ADD PRIMARY KEY (`posisi_id`);

--
-- Indexes for table `satuan`
--
ALTER TABLE `satuan`
  ADD PRIMARY KEY (`satuan_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posisi`
--
ALTER TABLE `posisi`
  MODIFY `posisi_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3002;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
